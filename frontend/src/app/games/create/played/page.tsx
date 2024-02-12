import CreatePlayedGameForm from '@/components/games/PlayedGameCreationForm'
import { Title } from '@mantine/core'

export default function AlreadyPlayedGamePage() {
  return (
    <>
      <Title order={1} fw={900} ta="center" mb={10}>
        Create a new Game
      </Title>
      <CreatePlayedGameForm />
    </>
  )
}
