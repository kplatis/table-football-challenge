import useTeams from '@/hooks/useTeams'
import {
  Button,
  Center,
  Group,
  Loader,
  Select,
  SimpleGrid,
} from '@mantine/core'
import { useForm } from '@mantine/form'

type Props = {
  setTeamsFn: (firstTeamId: number, secondTeamId: number) => void
}

export default function TeamSelectionForm({ setTeamsFn }: Props) {
  const { isLoading, data } = useTeams()

  const form = useForm({
    initialValues: {
      firstTeamId: null,
      secondTeamId: null,
    },
    validate: {
      firstTeamId: (value, values) =>
        values.secondTeamId &&
        value === values.secondTeamId &&
        'First and second team cannot be the same',
      secondTeamId: (value, values) =>
        values.firstTeamId &&
        value === values.firstTeamId &&
        'First and second team cannot be the same',
    },
  })

  const submit = (values: any) => {
    setTeamsFn(values.firstTeamId, values.secondTeamId)
  }

  if (isLoading) {
    return (
      <Center>
        <Loader color="blue" />
      </Center>
    )
  }
  if (data) {
    const teamsData = data.map((team) => ({
      value: team.id.toString(),
      label: team.name,
    }))

    return (
      <>
        <form onSubmit={form.onSubmit(submit)}>
          <SimpleGrid cols={2}>
            <Select
              label="First Team"
              name="firstTeamId"
              placeholder="Pick a team"
              data={teamsData}
              required={true}
              {...form.getInputProps('firstTeamId')}
            />

            <Select
              label="Second Team"
              name="secondTeamId"
              placeholder="Pick a team"
              data={teamsData}
              required={true}
              {...form.getInputProps('secondTeamId')}
            />
          </SimpleGrid>
          <Group justify="center" mt="md">
            <Button type="submit" size="md">
              Start the game!
            </Button>
          </Group>
        </form>
      </>
    )
  }
}
