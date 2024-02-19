import CreatePlayedGameForm from '@/components/games/PlayedGameCreationForm'
import { Title } from '@mantine/core'

export default function AlreadyPlayedGamePage() {
  return (
    <>
      <Title order={1} fw={900} ta="center" m="xl">
        Create a new Game
      </Title>
      <CreatePlayedGameForm />
    </>
  )
}
