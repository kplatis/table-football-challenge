'use client'

import { Button, Group, Modal, Select, Stack, TextInput } from '@mantine/core'
import { notifications } from '@mantine/notifications'
import { useForm } from '@mantine/form'
import usePlayers from '@/hooks/usePlayers'
import { validateFirstPlayer, validateSecondPlayer } from './validation'
import axios from 'axios'
import { TeamCreate } from '@/types/teams'
import PlayerCreationForm from '@/components/players/PlayerCreationForm'
import { useDisclosure } from '@mantine/hooks'
import Loader from '@/components/layout/Loader'

export default function TeamCreationForm() {
  const { isLoading, data, refetch } = usePlayers()
  const [opened, { open, close }] = useDisclosure(false)
  const form = useForm({
    initialValues: {
      name: '',
      firstPlayer: null,
      secondPlayer: null,
    },
    validate: {
      name: (value) => value.trim().length < 2,
      firstPlayer: validateFirstPlayer,
      secondPlayer: validateSecondPlayer,
    },
  })

  /**
   * Function called when the player is created.
   */
  const onPlayerCreated = () => {
    // close the modal
    close()
    // refetch players data
    refetch()
  }

  const submit = (values: any) => {
    const data: TeamCreate = {
      name: values.name,
      first_player_id: parseInt(values.firstPlayer, 10),
    }
    if (values.secondPlayer !== undefined) {
      data['second_player_id'] = parseInt(values.secondPlayer, 10)
    }

    axios.post('http://localhost:8000/teams', data).then((response) => {
      if (response.status === 200) {
        notifications.show({
          message: 'Success! Your team has been created.',
        })
        form.reset()
      }
    })
  }

  if (isLoading) {
    return <Loader />
  }
  if (data) {
    const playerData = data.map((player) => ({
      value: player.id.toString(),
      label: player.name,
    }))

    return (
      <>
        <Modal opened={opened} onClose={close} title="Create new Player">
          <PlayerCreationForm onSuccessFn={onPlayerCreated} />
        </Modal>
        <form onSubmit={form.onSubmit(submit)}>
          <Stack h={200} bg="var(--mantine-color-body)" gap="lg">
            <TextInput
              label="Name"
              placeholder="Team's name"
              name="name"
              variant="filled"
              required={true}
              data-testid="name-input"
              {...form.getInputProps('name')}
            />
            <Group justify="space-between">
              <Select
                label="First Player"
                name="firstPlayer"
                placeholder="Pick a player"
                data={playerData}
                required={true}
                data-testid="first-player-select"
                {...form.getInputProps('firstPlayer')}
              />

              <Select
                label="Second Player"
                name="secondPlayer"
                placeholder="Pick a player"
                data={playerData}
                data-testid="second-player-select"
                {...form.getInputProps('secondPlayer')}
              />

              <Button onClick={open} data-testid="create-new-player-button">
                Create new player
              </Button>
            </Group>
          </Stack>

          <Group justify="center" mt="md">
            <Button
              type="submit"
              size="md"
              data-testid="create-new-team-button"
            >
              Create Team
            </Button>
          </Group>
        </form>
      </>
    )
  }

  return <div>Players could not be loaded</div>
}
